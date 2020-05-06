import matplotlib.pyplot as plt
import pandas as pd

def clean_data_set(link):
    '''
    Retourne un dataFrame sans donnée vide.
    '''
    return pd.read_csv(link).ffill().bfill()

def fill_data(data, links):
    for link in links:
        csv_name = link.split('/')[-1].split('.')[0]
        data[csv_name] = clean_data_set(link)

def plot_data(data):

    fig, axes = plt.subplots(nrows=len(data.keys()), ncols=1, figsize=(20, 10))

    for csv_name, axis in zip(data.keys(), axes):
        csv = data[csv_name]

        end = len(csv['date'])
        beginning = end - 10
        days_step = 1

        countries = ['France', 'Italy', 'United Kingdom', 'China'] #, 'United States']
        '''
        countries = list(csv.keys())

        if 'date' in countries:
            countries.remove('date')
        if 'World' in countries:
            countries.remove('World')
        '''

        for country in countries:
            axis.plot(csv['date'][beginning:end], csv[country][beginning:end])
        
        title = csv_name[0].upper() + csv_name.replace('_', ' ')[1:]
        axis.title.set_text(title)

        axis.set_xticks(axis.get_xticks()[::days_step])

        for tick in axis.get_xticklabels():
            tick.set_rotation(45)

    axes[0].legend(bbox_to_anchor=(1.0,1))

    fig.tight_layout(h_pad=2.0)

    fig = plt.gcf()
    fig.canvas.set_window_title('Coronavirus DataViz')

    plt.show()

def main():
    links = [
        "https://covid.ourworldindata.org/data/ecdc/total_deaths.csv",
        "https://covid.ourworldindata.org/data/ecdc/new_cases.csv",
        "https://covid.ourworldindata.org/data/ecdc/new_deaths.csv",
        #"https://covid.ourworldindata.org/data/ecdc/full_data.csv",
        #"https://covid.ourworldindata.org/data/ecdc/locations.csv"
        # Useless for now
    ]

    data = {}

    fill_data(data, links)

    plot_data(data)

if __name__ == "__main__":
    main()
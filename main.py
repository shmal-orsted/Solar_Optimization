import os, pandas as pd
import requests
import requests_cache
from inputs.params import src_energy_manual_args as src_params
from functions import api_call, plotting
from inputs import params


def main():
    """
    This project will call the SRC api for multiple configurations to run optimization efforts.
    It will also produce analysis, visuals and data outputs from the returns from the API
    :param name: SRC_Key - this is an enviromental variable in my configuration but users will need to supply either a
    team or individual key to use this project, can't store this on Github
    :return:
    Data visualizations
    Analysis information
    etc. (TBD)
    """

    #TODO Input gathering (ini, gui, etc)
    # this is just going to be another input file for now (params.py)
    #may end up making another file for imports if this gets too messy

    # api call url
    src_energy_manual_url = r'https://api.src.dnv.com/api/site/energy-manual'

    # weather data file - just working for csv atm, will be changes
    weather_df = pd.read_csv(params.csv_filename, skiprows=3, names=['GHI', 'DHI', 'Tamb', 'Wspd'])

    # define gcr range, enter two numbers, inclusive lower end and exclusive upper end for use in api call loop
    gcr_range = [30, 45]

    # define dc, inclusive lower end and exclusive upper end range for use in api call loop
    dc_range = [200000, 300000]

    #TODO Setting up a cache to avoid extra API calls when we don't need them

    #TODO API Call
    json_dict, json_list = api_call.api_call_func(os.environ["API_KEY"], src_energy_manual_url, src_params, weather_df, gcr_range, dc_range)

    #TODO API Return Processing

    #TODO Imaging and Visualization (pyplot Graphs)

    plotting.plot_data(json_dict)

    #TODO Export Data, summarized and organized clearly


    #TODO GUI to do all this



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


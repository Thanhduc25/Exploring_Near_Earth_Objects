"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    # Initialize a dictionary to hold the NearEarthObjects, keyed by their designation
    neos = {}

    # Read the CSV file using the csv module
    with open(neo_csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            designation = row['pdes']
            name = row['name']
            diameter = float(row['diameter']) if row['diameter'] != '' else float('nan')
            hazardous = row['pha'] == 'Y'
            neo = NearEarthObject(designation=designation, name=name, diameter=diameter, hazardous=hazardous)

            # Add the NEO to the dictionary with its designation as the key
            neos[designation] = neo

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    with open(cad_json_path) as f:
        cad_data = json.load(f)
    # Define a list
    approach = []
    for approach_data in cad_data['data']:
        designation = str(approach_data[0]) if str(approach_data[0]) != 'None' else ''
        time = str(approach_data[3])
        distance = float(approach_data[4])
        velocity = float(approach_data[7])
        # Create a new `CloseApproach` object and append to the list
        approach_element = CloseApproach(designation=designation, time=time, distance=distance, velocity=velocity)
        approach.append(approach_element)

    return approach

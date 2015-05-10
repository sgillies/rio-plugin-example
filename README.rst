rio-plugin-example
==================

A Rasterio CLI command plugin example. 

.. image:: https://travis-ci.org/sgillies/rio-plugin-example.svg
   :target: https://travis-ci.org/sgillies/rio-plugin-example

Usage
-----

Given a path to a raster dataset, this project's `rio metasay` command prints a
picture of a cow saying one random or optionally specified (see `--item`)
metadata item from the dataset.

.. code-block:: console

    $ rio metasay tests/data/RGB.byte.tif
     ____________
    < Width: 791 >
     ------------
      \
       \   \_\_    _/_/
        \      \__/
               (oo)\_______
               (__)\       )\/\
                   ||----w |
                   ||     ||


This project is a recipe for new, actually useful plugins, and hopefully 
generates a few nostalgic chuckles or groans.

Installation
------------

If you've already 
`installed Rasterio <https://github.com/mapbox/rasterio#installation>`,
installation is just ``pip install rio-metasay``.

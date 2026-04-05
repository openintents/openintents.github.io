---
title: "Creating a Bitfari Map"
categories: blockstack
image:
  title: creating-a-bitfari-map.png
---

Bitfari creates a decentralized ad network that links virtual ads to physical locations. The physical locations are identified by Open Street Map (OSM) ids and the managers of these locations are registered on the Stacks blockchain.

In order to create a map with all registered locations, you have to follow the steps below:

- 

Run a stacks node and have access to the database e.g. via [stacksonchain.com](http://stacksonchain.com)

- 

Find all land nfts in the `nft_events` table for asset `SP213KNHB5QD308TEESY1ZMX1BP8EZDPG4JWD0MEA.web4::digital-land`

- 

For each nft read the map `transfer-utility` to find the OSM id

- 

Output the osm ids as overpass script

- 

Convert the overpass script on [https://overpass-turbo.eu/](https://overpass-turbo.eu/) to json

- 

Use the json in your web app containing the OSM map as markers. You can adopt most of the code from [Harry Wood](https://harrywood.co.uk/maps/examples/openlayers/marker-popups.view.html)

You can find the source code for step 1.- 4. at [here](https://gitlab.com/riot.ai/clarity-pool-tools/-/blob/master/tool-scripts/analysis-digital-land-2.ts).

The final result is a simple map with many markers: [https://digital-land-map.neocities.org/](https://digital-land-map.neocities.org/) (simple html page, easy to view the source code).

Feel free to inspect the source code and build something greater!

A git repo for work in progress was started [here](https://codeberg.org/friedger/bitfari-digital-land-map).

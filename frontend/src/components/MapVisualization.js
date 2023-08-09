import React from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

const MapVisualization = ({ pickup, dropoff, waypoints = [] }) => {

  const GOOGLE_API_KEY = "AIzaSyCgUqo-cXBIjuDBOY32soTmSRIF9xort2E"
    
  const containerStyle = {
    width: '100%',
    height: '400px'
  };

  const center = {
    lat: 42.2917,
    lng: -85.5872
  };

  const zoom = 13

  const position = {
    lat: 42.288692,
    lng: -85.616753
  }

  const onLoad = marker => {
    console.log('marker: ', marker)
  }

  return (
    <LoadScript googleMapsApiKey={GOOGLE_API_KEY}>
      <GoogleMap mapContainerStyle={containerStyle} center={center} zoom={zoom}>
        <Marker
        onLoad={onLoad}
        position={position}
        />
      </GoogleMap>
    </LoadScript>
  );
};

export default MapVisualization;

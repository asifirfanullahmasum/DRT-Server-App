import React, { useState } from 'react';
import FormGroup from '../components/FormGroup'
import Button from '../components/Button'
import MapVisualization from '../components/MapVisualization'

const ServicePage = () => {
    const [pickup, setPickup] = useState('');
    const [dropoff, setDropoff] = useState('');

    const [pickup_geocodes, setPickupGeocodes] = useState({});
    const [dropoff_geocodes, setDropoffGeocodes] = useState({});

    const pickuplocation = { lat: 42.288692, lng: -85.616753 };
    const dropofflocation = { lat: 42.277507, lng: -85.580142 };
    const waypoints = [
        { lat: 42.2921, lng: -85.6016 },
        { lat: 42.2787, lng: -85.5875 },
        { lat: 42.2836, lng: -85.6105 }
    ];

    const handleFormSubmit = (e) => {
        e.preventDefault();
      
        console.log('Pickup:', pickup);
        console.log('Dropoff:', dropoff);
      
        // Additional logic or API calls can be added here
    };
    const handlePickupChange = (e) => {
        setPickup(e.target.value);
        setPickupGeocodes({ lat: 42.288692, lng: -85.616753})
        checkFormValidity();
    };

    const handleDropoffChange = (e) => {
        setDropoff(e.target.value);
        setDropoffGeocodes({ lat: 42.277507, lng: -85.580142})
        checkFormValidity();
    };

    const checkFormValidity = () => {
        const requestRideBtn = document.getElementById('requestRideBtn');
        if (pickup && dropoff) {
            requestRideBtn.removeAttribute('disabled');
            requestRideBtn.classList.remove('disabled-button');
        } else {
            requestRideBtn.setAttribute('disabled', true);
            requestRideBtn.classList.add('disabled-button');
        }
    };

    return (
        <div className="map-container">
            <h1>Map Simulation</h1>
            <form onSubmit={handleFormSubmit}>
                <FormGroup label="Pickup Location">
                    <input
                        type="text"
                        id="pickup"
                        name="pickup"
                        placeholder="Enter pickup location"
                        value={pickup}
                        onChange={handlePickupChange}
                    />
                </FormGroup>
                <FormGroup label="Dropoff Location">
                    <input
                        type="text"
                        id="dropoff"
                        name="dropoff"
                        placeholder="Enter dropoff location"
                        value={dropoff}
                        onChange={handleDropoffChange}
                    />
                </FormGroup>
                <div className="map-form-group">
                    <Button
                        id="requestRideBtn"
                        type="submit"
                        disabled={!pickup || !dropoff}
                    >
                        Request a Ride
                    </Button>
                </div>
            </form>
            <div id="map">
                <MapVisualization pickup={pickup} dropoff={dropoff} waypoints={waypoints} />
            </div>
        </div>
    );
};

export default ServicePage;

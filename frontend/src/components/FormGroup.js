import React from 'react'

const FormGroup = ({ label, children }) => {
    return (
        <div className="map-form-group">
            <label htmlFor={label.toLowerCase()}>{label}:</label>
            {children}
        </div>
    )
}

export default FormGroup

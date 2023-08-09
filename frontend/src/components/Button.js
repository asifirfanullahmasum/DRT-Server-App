import React from 'react'

const Button = ({ id, type, disabled, children }) => {
    return (
        <button id={id} type={type} disabled={disabled} className={disabled ? 'disabled-button' : ''}>
            {children}
        </button>
    )
}

export default Button

import React from 'react';
import { Link } from 'react-router-dom';

export function Navigation() {
    return (
        <nav>
            <p>
                <Link to="/login">Login</Link>
            </p>
        </nav>
    );
};
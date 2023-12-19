import React, { useState } from 'react';
import Template from '../../../layouts/Template';

export function LoginPage() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleEmailChange = (e) => {
        setEmail(e.target.value);
    };

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Perform login logic here
        console.log('Email:', email);
        console.log('Password:', password);
    };

    return <Template>
        <section className="text-white w-[90%] md:w-[500px] flex-1 m-10">
            Formilario de registro

            <input type="datetime" name="" id="" />
        </section>
    </Template>
};

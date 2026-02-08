import React, { useState } from 'react';
import AuthForm from '../components/AuthForm';
import { login, register } from '../api';
import { useNavigate } from 'react-router-dom';

const LandingPage = () => {
    const [isLogin, setIsLogin] = useState(true);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    const handleAuth = async (data) => {
        setIsLoading(true);
        setError(null);
        try {
            if (isLogin) {
                const response = await login(data.username, data.password);
                localStorage.setItem('userId', response.user_id);
                navigate('/notes');
            } else {
                await register(data.username, data.password);
                setIsLogin(true); // Switch to login after successful registration
                setError('Registration successful! Please sign in.');
            }
        } catch (err) {
            const detail = err.response?.data?.detail;
            if (Array.isArray(detail)) {
                const errorMessages = detail.map(error => error.msg.replace('Value error, ', '')).join('. ');
                setError(errorMessages);
            } else {
                setError(detail || 'An error occurred. Please try again.');
            }
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-gradient-to-br from-mint-50 to-white flex flex-col items-center justify-center p-4">
            <div className="text-center mb-8">
                <h1 className="text-4xl md:text-5xl font-bold text-mint-900 mb-2 tracking-tight">Mic-Notes</h1>
                <p className="text-gray-500 text-lg">Your minimalist thought organizer.</p>
            </div>

            <div className="w-full max-w-sm">
                <AuthForm
                    type={isLogin ? 'login' : 'register'}
                    onSubmit={handleAuth}
                    isLoading={isLoading}
                    error={error}
                />

                <div className="mt-6 text-center">
                    <p className="text-gray-600">
                        {isLogin ? "Don't have an account? " : "Already have an account? "}
                        <button
                            onClick={() => {
                                setIsLogin(!isLogin);
                                setError(null);
                            }}
                            className="text-mint-600 font-semibold hover:underline"
                        >
                            {isLogin ? 'Sign up' : 'Login'}
                        </button>
                    </p>
                </div>
            </div>
        </div>
    );
};

export default LandingPage;

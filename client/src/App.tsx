import '@mantine/core/styles.css';

import { Routes, Route } from 'react-router-dom';

import { MantineProvider, Box } from '@mantine/core';
import LoginPage from './pages/LoginPage';
import UserPage from './pages/UserPage';



function App() {
    return (
        <MantineProvider>
            <Box bg="var(--mantine-color-gray-light)" mih={'100vh'}>
                <Routes>
                    <Route path='/login' element={<LoginPage />} />

                    <Route path='/' element={<UserPage />} />
                </Routes>
            </Box>
        </MantineProvider>
    )
}

export default App

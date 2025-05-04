import React from 'react'
import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'

import { apiGet } from '../utils/api'

import { Center, Paper, Title, Group, Button, Avatar, Stack } from '@mantine/core'

const UserPage = () => {
    const navigate = useNavigate()
    const [user, setUser] = useState({ username: null, id: null, })


    useEffect(() => {
        apiGet("/users")
            .then((result) => {
                setUser(result?.data?.user)
            })
            .catch((error) => {
                console.log(error)
                navigate("/login")
            })
    }, [])



    const handleLogoutClick = async () => {
        apiGet("/logout")
            .then((result) => {
                navigate("/login")
            })
            .catch((error) => {
                console.log(error)
            })
    }



    return (
        <Center mih={'100vh'}>
            <Paper shadow='sm' p='xl' miw={400}>
                <Group justify="space-between">
                    <Title order={2}>
                        Profile
                    </Title>

                    <Button variant="transparent" onClick={handleLogoutClick}>
                        Logout
                    </Button>
                </Group>

                <Stack
                    h={200}
                    align="stretch"
                    justify="center"
                    gap="md"
                >
                    <Group justify="start">
                        <Avatar size={'xl'} name={`${user?.username}`} color="initials" />

                        <Title order={3}>
                            {user?.username}
                        </Title>
                    </Group>
                </Stack>
            </Paper>
        </Center>
    )
}

export default UserPage
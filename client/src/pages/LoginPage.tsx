import React from 'react'
import { useForm } from '@mantine/form'
import { useNavigate } from 'react-router-dom'

import { apiPost } from '../utils/api'

import { Stack, Center, Input, Paper, PasswordInput, Button, Title } from '@mantine/core'



const LoginPage = () => {
    const navigate = useNavigate()


    const form = useForm({
        mode: 'uncontrolled',
        initialValues: {
            username: "",
            password: "",
        },
    })



    const handleSubmit = async (body: object = {}) => {
        try {
            const result = await apiPost("/login", body)

            if (Boolean(result)) {
                navigate("/")
            }
        } catch (error) {
            console.log(error)
        }
    }



    return (
        <Center mih={'100vh'}>
            <Paper shadow='sm' p='xl' miw={400}>
                <Title order={2}>
                    Authentication Module
                </Title>
                <form
                    onSubmit={form.onSubmit((values) => handleSubmit(values))}
                >
                    <Stack
                        h={250}
                        align="stretch"
                        justify="center"
                        gap="md"
                    >

                        <Input.Wrapper label="Your login">
                            <Input
                                w={'100%'}
                                placeholder="username"
                                key={form.key('username')}
                                {...form.getInputProps('username')}
                            />
                        </Input.Wrapper>

                        <PasswordInput
                            w={'100%'}
                            label="Your password"
                            placeholder="password"
                            key={form.key('password')}
                            {...form.getInputProps('password')}
                        />

                        <Button type="submit">
                            Log in
                        </Button>
                    </Stack>
                </form>
            </Paper>
        </Center>
    )
}

export default LoginPage
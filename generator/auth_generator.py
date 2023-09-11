from util import folder_creator
class GenAuth:

    def __init__(self, base_dir) -> None:
        self.base_dir = base_dir

    def __generate(self):
        self.result = """
import { test as setup, expect } from '@playwright/test';


setup('authenticate', async ({ request }) => {
    // your logic to getting access token
    const accessToken = ""
    process.env.AUTH = accessToken
});
"""
        folder_creator(self.base_dir+'/config/')
        with open(self.base_dir+'/config/auth.setup.ts', 'w') as file:
            file.write(self.result)
    
    def __str__(self) -> str:
        self.__generate()
        return "Auth file has been created 😄"

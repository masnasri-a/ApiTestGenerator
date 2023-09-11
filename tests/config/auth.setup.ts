
import { test as setup, expect } from '@playwright/test';


setup('authenticate', async ({ request }) => {
    // your logic to getting access token
    const accessToken = ""
    process.env.AUTH = accessToken
});

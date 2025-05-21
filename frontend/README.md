## Getting Started

This guide explains how to use the frontend interface to manage your data and view optimization results.

---

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Navigation

Use the sidebar to easily navigate to different sections of the application:

* **Home**: Displays a welcome message.
* **Customers**: Manage customer records.
* **Vehicles**: Manage vehicle records.
* **Parts**: Manage your parts inventory.
* **Repair Orders**: Manage repair order details.
* **Order Details**: Manage specific details within repair orders.
* **Optimize**: Run and view optimization results.

---

## Entity Management Interface

Each entity page (e.g., `/customers`, `/vehicles`) features a consistent layout:

* **Form**: Located at the top, this is where you enter data to **create new records** or **update existing ones**. Fields are clearly labeled (e.g., "Name", "Part Number") and include **type validation** (e.g., numbers for IDs, dates for date fields).
* **Table**: Below the form, you'll find a table displaying your existing records. It includes columns for all relevant fields (e.g., ID, Name for customers). Each row also has a **Delete button** to remove a record.

### Usage Example (for Customers)

1.  Go to `http://localhost:3000/customers`.
2.  In the form, enter details like **Name: “Jane”** and **Last Name: “Smith”**.
3.  Click **Submit** to create the new customer record.
4.  The table will automatically update to show the newly added customer.
5.  To remove a customer, simply click the **Delete** button on their row.

---

## Optimization Results Display

To view optimized repair orders:

1.  Navigate to `http://localhost:3000/optimize`.
2.  Click the **Run Optimization** button. This will fetch the optimized repair orders from the backend.
3.  The results will appear in a table, displaying each order’s **ID**, **Vehicle ID**, **Start Date**, **Status**, **Labor Cost**, and **Priority**.

**Note**: For meaningful results, ensure your backend has **pending repair orders** and **sufficient parts in the inventory**.

---

## Testing and Interaction

It's a good practice to test the application's functionality.

### Test CRUD Operations

For each entity page, perform **Create, Read, Update, and Delete (CRUD)** operations:

1.  **Create** a few records using the form.
2.  **Verify** they appear in the table.
3.  **Delete** them using the Delete button.

#### Example for Parts:

1.  Go to `/parts`.
2.  Add a new part (e.g., **Part Number: “P001”**, **Description: “Brake Pad”**, **Stock: 10**, **Cost: 25.99**).
3.  Check the table to confirm the part is listed.
4.  Delete the part and verify its removal.

### Test Optimization

1.  Ensure your backend has **multiple pending repair orders** with associated order details and parts.
2.  Navigate to `/optimize`.
3.  Click **Run Optimization**.
4.  Verify that the table displays the selected orders, correctly prioritized by the `prioridad` field.

### Debugging

If you encounter issues:

* **No data on a page?** Check your browser’s **DevTools** (F12, Network tab) for any failed API requests.
* **404 error?** Make sure `pages/index.js` exists and your server is running (`npm run dev`).
* **Backend not responding?** Confirm that your backend service is running and the `apiClient.js` URL is correct.

---

## Troubleshooting

Here are some common issues and their solutions:

* **404 Page Not Found**:
    * Ensure `pages/index.js` exists and contains the necessary code.
    * **Restart the server** by running `npm run dev`.
* **Empty Tables**:
    * Verify that your backend has data. You can check this using **Swagger UI** at `http://localhost:8000/docs`.
    * Check the `useEffect` calls in your `pages` components (e.g., `customers.js`) to ensure they are calling the correct API endpoints.
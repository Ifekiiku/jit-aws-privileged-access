## 📌 Notes on EXPRESS Workflow (Optional Enhancement)

# It’s possible to return the credentials instantly via API by:
- Deleting the Standard Step Function
- Re-creating the same workflow as Express type
- Changing Lambda from start_execution() to start_sync_execution()
- The Lambda would then return credentials directly in the API response

❗ This incurs additional costs per request + duration.

Reason not used in this project: Cost-efficiency. The Standard version is asynchronous but cheaper and good enough for low-volume requests.
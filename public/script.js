document.getElementById('task-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const form = e.target;
  const data = new FormData(form);
  const res = await fetch('/api/query', {
    method: 'POST',
    body: data
  });
  const json = await res.json();
  document.getElementById('content-frame').textContent = JSON.stringify(json, null, 2);
});

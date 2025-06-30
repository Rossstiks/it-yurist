const express = require('express');
const multer  = require('multer');
const path = require('path');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(express.static(path.join(__dirname, 'public')));

app.post('/api/query', upload.single('file'), (req, res) => {
  const task = req.body.task || '';
  // TODO: интеграция с Gemini AI и поиск по страницам
  res.json({
    message: 'Заглушка API',
    task,
    tags: ['пример']
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});

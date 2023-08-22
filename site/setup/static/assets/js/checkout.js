// Exemplo de JavaScript inicial para desabilitar envios de formulário se houver campos inválidos
(() => {
  'use strict'

  // Buscar todos os formulários aos quais queremos aplicar estilos personalizados de validação de Bootstrap
  const forms = document.querySelectorAll('.needs-validation')

  // Passe por cima deles e impeça a submissão
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false)
  })
})()
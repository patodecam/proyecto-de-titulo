document.addEventListener('DOMContentLoaded', function() {
  const calendarEl = document.getElementById('calendar');
  const calendar = new FullCalendar.Calendar(calendarEl, {
    themeSystem: 'bootstrap5',
    headerToolbar: {
      left: 'prevYear,prev,next,nextYear today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay'
    },
    buttonText: {
      today: 'Hoy',
      month: 'Mes',
      week: 'Semana',
      day: 'Día',
      list: 'Lista'
    },
    titleFormat: { year: 'numeric', month: 'long', day: 'numeric' },
    navLinks: true,
    editable: true,
    selectable: true,
    selectMirror: true,
    locale: 'es',
    eventColor: '#378006',
    events: [
      { title: 'Meeting', start: new Date() }
    ],

    select: function(arg) {
      const title = prompt('Título del Evento:');
      if (title) {
        calendar.addEvent({
          title: title,
          start: arg.start,
          end: arg.end,
          allDay: arg.allDay
        });
      }
      calendar.unselect();
    },

    eventClick: function(arg) {
      if (confirm('¿Estás seguro de que deseas eliminar este evento?')) {
        arg.event.remove();
      }
    },

    eventMouseEnter: function(info) {
      const tooltip = new Tooltip(info.el, {
        title: info.event.title,
        placement: 'top',
        trigger: 'hover',
        container: 'body'
      });
    },

    eventMouseLeave: function(info) {
      const tooltip = new Tooltip(info.el);
      tooltip.dispose();
    },

    customButtons: {
      addEventButton: {
        text: 'Añadir Evento',
        click: function() {
          const dateStr = prompt('Ingrese una fecha en formato YYYY-MM-DD');
          const date = new Date(dateStr + 'T00:00:00'); // will be in local time
          if (!isNaN(date.valueOf())) {
            calendar.addEvent({
              title: 'Evento Añadido',
              start: date,
              allDay: true
            });
            alert('Evento añadido.');
          } else {
            alert('Fecha inválida.');
          }
        }
      }
    }
  });

  calendar.render();
});

$(function () {

    $('#calendar').fullCalendar({
        defaultView: 'agendaSevenDay',
        groupByResource: true,
        defaultDate: '2019-02-18',
        events: [
            {
                title: 'CONSEJO DE ESCUELA/ COMISION CURRICULAR',
                start: '2019-02-20T10:00:00',
                end: '2019-02-20T11:00:00'
            },
            {
                title: 'CONSEJO DE ESCUELA/ COMISION CURRICULAR',
                start: '2019-02-20T11:00:00',
                end: '2019-02-20T12:00:00'
            },
            {
                title: 'CONSEJO DE ESCUELA/ COMISION CURRICULAR',
                start: '2019-02-20T12:00:00',
                end: '2019-02-20T13:00:00'
            },
            {
                title: 'REUNION DE INVESTIGACION',
                start: '2019-02-21T13:00:00',
                end: '2019-02-21T14:00:00'
            },
            {
                title: 'REUNION DE INVESTIGACION',
                start: '2019-02-21T14:00:00',
                end: '2019-02-21T15:00:00'
            },
            {
                title: 'REUNION DE INVESTIGACION',
                start: '2019-02-21T15:00:00',
                end: '2019-02-21T16:00:00'
            },
            {
                title: 'REUNIÓN DE POSTGRADO C/15 DIAS',
                start: '2019-02-22T09:00:00',
                end: '2019-02-22T10:00:00'
            },
            {
                title: 'REUNIÓN DE POSTGRADO C/15 DIAS',
                start: '2019-02-22T10:00:00',
                end: '2019-02-22T11:00:00'
            },
            {
                title: 'REUNIÓN DE POSTGRADO C/15 DIAS',
                start: '2019-02-22T11:00:00',
                end: '2019-02-22T12:00:00'
            },
            {
                title: 'REUNIÓN DE POSTGRADO C/15 DIAS',
                start: '2019-02-22T12:00:00',
                end: '2019-02-22T13:00:00'
            },
            
            {
                title: 'CONSEJO DE ESCUELA/ COMISION CURRICULAR',
                start: '2019-02-27T10:00:00',
                end: '2019-02-27T11:00:00'
            },
            {
                title: 'CONSEJO DE ESCUELA/ COMISION CURRICULAR',
                start: '2019-02-27T11:00:00',
                end: '2019-02-27T12:00:00'
            },
            {
                title: 'CONSEJO DE ESCUELA/ COMISION CURRICULAR',
                start: '2019-02-27T12:00:00',
                end: '2019-02-27T13:00:00'
            },
            {
                title: 'REUNION DE INVESTIGACION',
                start: '2019-02-28T13:00:00',
                end: '2019-02-28T14:00:00'
            },
            {
                title: 'REUNION DE INVESTIGACION',
                start: '2019-02-28T14:00:00',
                end: '2019-02-28T15:00:00'
            },
            {
                title: 'REUNION DE INVESTIGACION',
                start: '2019-02-28T15:00:00',
                end: '2019-02-28T16:00:00'
            },
            {
                title: 'REUNIÓN DE POSTGRADO C/15 DIAS',
                start: '2019-03-01T09:00:00',
                end: '2019-03-01T10:00:00'
            },
            {
                title: 'REUNIÓN DE POSTGRADO C/15 DIAS',
                start: '2019-03-01T10:00:00',
                end: '2019-03-01T11:00:00'
            },
            {
                title: 'REUNIÓN DE POSTGRADO C/15 DIAS',
                start: '2019-03-01T11:00:00',
                end: '2019-03-01T12:00:00'
            },
            {
                title: 'REUNIÓN DE POSTGRADO C/15 DIAS',
                start: '2019-03-01T12:00:00',
                end: '2019-03-01T13:00:00'
            },

            {
                title: 'CONSEJO DE ESCUELA/ COMISION CURRICULAR',
                start: '2019-03-06T10:00:00',
                end: '2019-03-06T11:00:00'
            },
            {
                title: 'CONSEJO DE ESCUELA/ COMISION CURRICULAR',
                start: '2019-03-06T11:00:00',
                end: '2019-03-06T12:00:00'
            },
            {
                title: 'CONSEJO DE ESCUELA/ COMISION CURRICULAR',
                start: '2019-03-06T12:00:00',
                end: '2019-03-06T13:00:00'
            },
            {
                title: 'REUNION DE INVESTIGACION',
                start: '2019-03-07T13:00:00',
                end: '2019-03-07T14:00:00'
            },
            {
                title: 'REUNION DE INVESTIGACION',
                start: '2019-03-07T14:00:00',
                end: '2019-03-07T15:00:00'
            },
            {
                title: 'REUNION DE INVESTIGACION',
                start: '2019-03-07T15:00:00',
                end: '2019-03-07T16:00:00'
            },
            {
                title: 'REUNIÓN DE POSTGRADO C/15 DIAS',
                start: '2019-03-08T09:00:00',
                end: '2019-03-08T10:00:00'
            },
            {
                title: 'REUNIÓN DE POSTGRADO C/15 DIAS',
                start: '2019-03-08T10:00:00',
                end: '2019-03-08T11:00:00'
            },
            {
                title: 'REUNIÓN DE POSTGRADO C/15 DIAS',
                start: '2019-03-08T11:00:00',
                end: '2019-03-08T12:00:00'
            },
            {
                title: 'REUNIÓN DE POSTGRADO C/15 DIAS',
                start: '2019-03-08T12:00:00',
                end: '2019-03-08T13:00:00'
            }
            
        ],
        header: {
            left: 'prev,next',
            center: 'title',
            right: 'agendaDay,agendaSevenDay'
        },
        views: {
            agendaSevenDay: {
                type: 'agenda',
                hiddenDays: [0, 6],
                minTime: "07:00:00",
                maxTime: "21:00:00",
                duration: { days: 7 }
            }
        },
        navLinks: false, // can click day/week names to navigate views
        editable: false,
        eventLimit: false, // allow "more" link when too many events
        slotDuration: "00:15:00",

    });
    $('#calendar').fullCalendar('option', 'height', 550);
    $('#calendar').fullCalendar('updateEvent', {

        events: [
            {
                title: 'Event Title1 haskdjk',
                start: '2019-02-20T13:00:00',
                end: '2019-02-20T17:00:00'
            }
        ]
    }
    )
});
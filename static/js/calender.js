$(function () {

    $('#calendar').fullCalendar({
        defaultView: 'agendaSevenDay',
        groupByResource: true,
        header: {
            left: 'prev,next',
            center: 'title',
            right: 'agendaDay,agendaSevenDay'
        },
        views: {
            agendaSevenDay: {
                type: 'agenda',
                hiddenDays: [5, 6],
                minTime: "07:00:00",
                maxTime: "21:00:00",
                duration: { days: 7 }
            }
        }
    });
    $('#calendar').fullCalendar('option', 'height', 550);
});
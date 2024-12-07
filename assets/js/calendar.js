/**
 * Displays the office hours and weekly calendars using
 * FullCalendar with Google Calendars integration.
 **/

var apiKey = 'AIzaSyBZKnVt7lMUmk0E2odYaPUHEO7iDTSBWOM';

// Change event url to null.
var transform = function(event) {
    event.url = null;
    return event;
}

// Add location to event display.
var render = function(event, element, view) {
    element.append($('<div class="fc-location">').html(event.location));
    return element;
}

// Show the current week during the semester and the first week of class otherwise.
function calendarStartDate() {
    if (moment().isBefore(moment(endDate)) && moment().isAfter(moment(startDate))) {
        return moment();
    }
    return startDate;
}

//General config for both weekly and office hours calendars
const calendarConfig = {
    eventDataTransform: transform,
    eventRender: render,
    eventMouseover: function(info) {
        if (info.location && info.location.includes("https://")) {
            $(this).css('cursor','pointer');
        }
    },
    eventMouseout: function(info) {
        if (info.location && info.location.includes("https://")) {
            $(this).css('cursor','auto');
        }
    },
    eventClick: function(info) {
        if (info.location && info.location.includes("https://")) {
            window.open(info.location);
        }
      },
    defaultView: $(window).width() >= 768 ? 'agendaWeek' : 'agendaDay',
    allDaySlot: false,
    slotEventOverlap: false,
    height: "auto",
    defaultDate: calendarStartDate(),
    googleCalendarApiKey: apiKey,
}

$(document).ready(function() {
    $('#office-hours').fullCalendar({
        ...calendarConfig,
        hiddenDays: [],
        minTime: "08:00:00",
        maxTime: "24:00:00",
        eventSources: [
            {
                googleCalendarId: officeHoursCalendarId,
                cache: true,
                color: '#0072c1'
            },
            {
                googleCalendarId: instructorOfficeHoursCalendarId,
                cache: true,
                color: '#004090'
            },
            {
                googleCalendarId: lecturesCalendarId,
                cache: true,
                color: '#c1d6e3',
                textColor: '#000'
            }
        ]
    });

    $('#weekly').fullCalendar({
        ...calendarConfig,
        weekends: true,
        minTime: "08:00:00",
        maxTime: "24:00:00",
        eventSources: [
            {
                googleCalendarId: sectionsCalendarId,
                cache: true,
                color: '#0072c1'
            },
            {
                googleCalendarId: lecturesCalendarId,
                cache: true,
                color: '#c1d6e3',
                textColor: '#000'
            },
        ]
    });
});

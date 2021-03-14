const canAttendMeetings = function (intervals) {
    // Write your code here
    _intervals = intervals.sort((a, b) => a.start - b.start);

    for (let i = 1; i < intervals.length; i++){
        if (_intervals[i - 1].end > _intervals[i].start)
            return false;
    }
    return true;
}
export default class ShiftRequest {
    constructor(numOfEmployees, numOfDays, numOfShifts) {
        this.numOfEmployees = numOfEmployees;
        this.numOfDays = numOfDays;
        this.numOfShifts = numOfShifts;
        this.shifts = {};
        for (let e = 0; e < numOfEmployees; e++) {
            this.shifts['e_' + e] = {};
            for (let d = 0; d < numOfDays; d++) {
                this.shifts['e_' + e]['d_' + d] = {};
                for (let s = 0; s < numOfShifts; s++) {
                    this.shifts['e_' + e]['d_' + d]['s_' + s] = false;
                }
            }
        }
    }
}

function createShiftRequestsArray(e, d, s) {
    return new Array(e).fill(
        new Array(d).fill(
            new Array(s).fill(false)
        )
    )
}

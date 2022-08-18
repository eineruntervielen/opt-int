<template>
  <div class="h-screen w-screen bg-sky-600">
    <div class="grid grid-cols-3 p-40">
      <Card class="m-1">
        <label>NrDays</label>
        <input
            class="shadow border rounded text-gray-700 py-1 px-3 hover:shadow-inner transition"
            type="number" min="1" step="1" max="7"
            v-model="numberOfDays" @keyup="updateShiftRequests"
        />
      </Card>
      <Card class="m-1">
        <label>Shifts</label>
        <input
            class="shadow border rounded text-gray-700 py-1 px-3 hover:shadow-inner transition"
            type="number" min="1" step="1" max="3"
            v-model="numberOfShifts" @keyup="updateShiftRequests"
        />
      </Card>
      <Card class="m-1">
        <label>Employees</label>
        <input
            class="shadow border rounded text-gray-700 py-1 px-3 hover:shadow-inner transition"
            type="number" min="1" step="1" max="10"
            v-model="numberOfEmployees" @keyup="updateShiftRequests"
        />
      </Card>
      <Card class="m-1 col-span-3">
        <table class="border-separate border-spacing-2 border border-slate-900">
          <thead class="border-slate-900">
          <tr>
            <th class="border " v-for="day in numberOfDays" :key="day">Day {{ day }}</th>
          </tr>
          </thead>
          <tbody>
          <tr
              v-for="(emp, eidx) in numberOfEmployees"
              :key="emp">
            <td
                class="border"
                v-for="(day, didx) in numberOfDays"
                :key="day">
              <input
                  class="w-10 m-2"
                  type="checkbox"
                  v-for="(shift, sidx) in numberOfShifts"
                  :key="shift"
                  v-model="shiftRequests[eidx][didx][sidx].value"
              >
            </td>
          </tr>
          </tbody>
        </table>
      </Card>
      <div>
        <button
            class=" shadow mx-auto border bg-slate-100 hover:bg-slate-200 rounded full text-gray-700 px-4 hover:scale-110 transition"
            @click="solve">
          Solve
        </button>
      </div>
    </div>
  </div>
</template>

<script>
const backendURL = "/api/staffscheduling/";
const initialNumDays = 5;
const initialNumShifts = 3;
const initialNumEmployees = 3;

function createShiftRequests(e, d, s) {
  let arr = new Array(e).fill(
      new Array(d).fill(
          new Array(s).fill(false)
      )
  )
  return arr
}

export default {
  name: "StaffScheduling",
  data() {
    return {
      shiftRequests: createShiftRequests(initialNumEmployees, initialNumDays, initialNumShifts),
      numberOfEmployees: initialNumEmployees,
      numberOfDays: initialNumDays,
      numberOfShifts: initialNumShifts,
    }
  },
  methods: {
    updateShiftRequests() {
      this.shiftRequests = createShiftRequests(this.numberOfEmployees, this.numberOfDays, this.numberOfShifts)
    },
    solve() {
      const backendData = {
        num_employees: this.numberOfEmployees,
        num_days: this.numberOfDays,
        num_shifts: this.numberOfShifts,
        shifts: this.shiftRequests
      };
      console.log(backendData)
      fetch(backendURL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(backendData),
      }).then((response) => response.json()
      ).then((data) => {
        console.log('Success:', data);
      }).catch((error) => {
        console.error('Error:', error);
      });

    }
  }
}
</script>

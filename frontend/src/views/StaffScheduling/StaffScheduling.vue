<template>
  <div class="h-screen w-screen">
    <div class="grid grid-cols-3 p-40">
      <Card class="m-1">
        <label class="px-1 text-sm font-bold text-gray-700">Nr. of days</label>
        <input
            class="shadow border rounded text-gray-700 py-1 px-3 hover:shadow-inner transition"
            type="number" min="1" step="1" max="7"
            v-model="numberOfDays" @keyup="updateShiftRequests"
        />
      </Card>
      <Card class="m-1">
        <label class="px-1 text-sm font-bold text-gray-700">Nr. of shifts</label>
        <input
            class="shadow border rounded text-gray-700 py-1 px-3 hover:shadow-inner transition"
            type="number" min="1" step="1" max="3"
            v-model="numberOfShifts" @keyup="updateShiftRequests"
        />
      </Card>
      <Card class="m-1">
        <label class="px-1 text-sm font-bold text-gray-700">Nr. of employees</label>
        <input
            class="shadow border rounded text-gray-700 py-1 px-3 hover:shadow-inner transition"
            type="number" min="1" step="1" max="10"
            v-model="numberOfEmployees" @keyup="updateShiftRequests"
        />
      </Card>
      <Card class="m-1 col-span-3">
        <table class="border-separate border-spacing-2 border">
          <thead>
          <tr>
            <th class="border" v-for="(day, dayIndex) in shiftRequests[0].length" :key="day">Day {{ dayIndex }}</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(emp, empIndex) in shiftRequests.length"
              :key="emp">
            <td v-for="(day, dayIndex) in shiftRequests[empIndex].length"
                :key="day"
                class="border">
              <input v-for="(shift, shiftIndex) in shiftRequests[empIndex][dayIndex].length"
                     :key="shift"
                     :id="'e_' + empIndex + '_d_' + dayIndex + '_s_' + shiftIndex"
                     v-model="shiftRequests[empIndex][dayIndex][shiftIndex]"
                     class="w-10 m-2 checked:shadow-xl"
                     type="checkbox"
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
const initialNumEmployees = 5;

function createShiftRequests(e, d, s) {
  return Array.from(Array(e),
      () => Array.from(Array(d),
          () => Array.from(Array(s),
              () => false)
      ))
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

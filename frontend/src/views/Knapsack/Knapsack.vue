<template>
  <div class="flex-grow p-8">
    <div class="flex">
      <InputText class="mx-2 p-inputtext-sm" placeholder="Instance name" v-model="kp.name"/>
      <InputNumber class="mx-2 shadow p-inputtext-sm" placeholder="Total capacity" v-model="kp.capacities"/>
      <InputNumber v-model="size"
                   class="mx-2 shadow p-inputtext-sm"
                   @input="updateRows"
                   showButtons buttonLayout="horizontal"
                   decrementButtonClass="p-button"
                   incrementButtonClass="p-button"
                   incrementButtonIcon="pi pi-plus"
                   decrementButtonIcon="pi pi-minus"
      />
      <div class="ml-auto">
        <Button class="ml-auto shadow" label="Solve knapsack problem" icon="pi pi-chevron-right" @click="postModel"/>
      </div>
    </div>
    <div class="shadow-sm mt-10">
      <DataTable :value="rows" editMode="cell" @cell-edit-complete="onCellEditComplete" class="editable-cells-table"
                 responsiveLayout="scroll">
        <template #header>
          <div class="table-header">
            Input data:<span class="text-sm ml-8 uppercase">{{ kp.name }}</span>
          </div>
        </template>
        <Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field" style="width:25%">
          <template #editor="{ data, field }">
            <InputText v-model="data[field]" autofocus/>
          </template>
        </Column>
      </DataTable>
    </div>
  </div>
  {{ result }}
</template>

<script>
const backendURL = "/api/knapsack";
// let kp_capacities = 850;
// let kp_weights = [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0, 42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71, 3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13]
// let kp_values = [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147, 78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28, 87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276, 312]
export default {
  name: "Knapsack.vue",
  methods: {
    async postModel() {
      fetch(backendURL, {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(this.kp)
          }
      ).then(r => r.json()).then(data => this.result = data)
    },
    onCellEditComplete(event) {
      let {data, newValue, field} = event;
      data[field] = newValue;
    },
    buildRows() {
      let tmp = [];
      for (let idx = 0; idx < this.size; idx++) {
        tmp[idx] = {
          nr: idx,
          weight: null,
          value: null
        }
        this.kp.weights[0].push(null);
        this.kp.values.push(null);
      }
      this.rows = tmp
    },
    updateRows(event) {
      if (event.value < event.formattedValue) {
        console.log('decrement')
        this.rows = this.rows.slice(0, event.value);
      } else {
        console.log('increment')
        let tmp = {
          nr: event.value,
          weight: null,
          value: null
        }
        this.kp.weights[0].push(null);
        this.kp.values.push(null);
      }
      console.log(this.kp);
      this.buildRows();

    },
  },
  data() {
    return {
      rows: null,
      columns: [
        {field: 'nr', header: 'Nr.'},
        {field: 'weight', header: 'Weight'},
        {field: 'value', header: 'Value'}
      ],
      kp: {
        name: "Test instance",
        capacities: [100],
        weights: [[]],
        values: [],
      },
      result: {
        weight: 0,
      },
      size: 3,
    }
  },
  mounted() {
    this.buildRows()
  }

}
</script>
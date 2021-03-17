<template>
    <div>
      <p>{{ msg }}</p>
      <p>{{ `${tester.no} and ${tester.yes}` }}</p>
    </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: 'Hello!',
      tester: {
        no: 'hello',
        yes: 'goodbye',
      },
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/api/test/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

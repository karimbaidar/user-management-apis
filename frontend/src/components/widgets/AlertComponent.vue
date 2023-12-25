<template>
    <div v-if="message" class="bg-red-100 border-t-4 border-red-500 rounded-b px-4 py-3 shadow-md mt-4">
      <div class="flex items-center">
        <div class="text-sm">
          <p>{{ message }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      message: String,
    },
  };
  </script>
  
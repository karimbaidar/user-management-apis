<template>
  <div
    class="flex flex-col items-center bg-white p-5 rounded shadow mx-auto w-full max-w-md"
  >
    <img
      v-if="avatar"
      :src="user[avatar]"
      alt="User Avatar"
      class="w-24 h-24 rounded-full mb-4"
    />
    <div v-for="field in fields" :key="field.key">
      <p class="text-gray-600">
        {{ field.label }}:
        <span class="font-medium">{{ user[field.key] }}</span>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    user: {
      type: Object,
      required: true,
    },
    fields: {
      type: Array,
      required: true,
    },
    avatar: {
      type: String,
      default: null,
    },
  },
};
</script>

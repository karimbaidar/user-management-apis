<template>
  <div class="relative">
    <button
      @click="toggleDropdown"
      class="w-full p-2 border border-gray-300 rounded-md flex items-center justify-between"
    >
      <img
        :src="selectedItem"
        alt="Selected Item"
        class="h-6 w-6 rounded-full"
        v-if="user.avatar"
      />
      <slot name="placeholder">
        <span class="text-gray-500">Select an Item</span>
      </slot>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        class="h-6 w-6 ml-auto"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M19 9l-7 7-7-7"
        />
      </svg>
    </button>
    <div
      class="absolute left-0 w-full mt-1 bg-white border border-gray-300 rounded-md shadow-lg"
      v-if="isOpen"
    >
      <div
        class="dropdown-item flex items-center space-x-2 p-2 hover:bg-gray-100 cursor-pointer"
        v-for="item in options"
        :key="item"
        @click="
          selectItem(item);
          isOpen = false;
        "
      >
        <img :src="item" alt="Item" class="h-6 w-6 rounded-full" />
        <span>{{ item }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    user: Object,
    selectedItem: String,
    isOpen: Boolean,
    options: Array,
    toggleDropdown: Function,
    selectItem: Function,
  },
};
</script>

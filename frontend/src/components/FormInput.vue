<template>
  <div
    class="flex flex-col md:flex-row items-center rounded px-2 border border-gray-300"
  >
    <slot name="icon" class="mr-2 md:mr-0 md:mb-0 mb-2"></slot>
    <input
      :type="type"
      :value="modelValue"
      @input="update"
      class="flex-1 border-none outline-none px-1 rounded"
      :placeholder="placeholder"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";

export default defineComponent({
  props: {
    modelValue: {
      type: String as PropType<string>,
      required: true,
    },
    type: {
      type: String as PropType<string>,
      default: "text",
    },
    placeholder: String,
  },
  setup(props, { emit }) {
    const update = (event: Event) => {
      emit("update:modelValue", (event.target as HTMLInputElement).value);
    };

    return {
      update,
    };
  },
});
</script>

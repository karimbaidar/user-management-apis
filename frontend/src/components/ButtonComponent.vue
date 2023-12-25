<template>
  <button @click="handleClick">
    <slot></slot>
  </button>
</template>

<script>
export default {
  setup(props, context) {
    const handleClick = () => {
      context.emit("click");
    };

    return {
      handleClick,
    };
  },
};
</script>

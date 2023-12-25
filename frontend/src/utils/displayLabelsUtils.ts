import { computed } from "vue";

const createComputedProperty = (keyValuePairs) => {
  return computed(() => {
    return keyValuePairs;
  });
};

export { createComputedProperty };

<template>
  <div class="flex flex-col my-8 p-1">
    <router-link
      v-for="item in visibleItems"
      :to="'/user/' + item.id"
      :key="item.id"
      @click="$emit('item-clicked', item)"
    >
      <div class="p-4 mb-4 rounded-md border border-gray-300 hover:bg-gray-100">
        <div class="px-4 py-2 flex flex-col lg:flex-row">
          <div
            class="flex flex-col lg:flex-1"
            v-for="(key, value) in filteredItem(item)"
            :key="key"
          >
            <div class="text-center py-2 font-bold">{{ key }}</div>
            <div class="text-center py-2">{{ value }}</div>
          </div>
        </div>
      </div>
    </router-link>
    <button v-if="visibleItems.length < items.length" @click="loadMore">
      Load More
    </button>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, ref, computed } from "vue";

export default defineComponent({
  props: {
    items: {
      type: Array as PropType<any[]>,
      required: true,
    },
    displayLabels: {
      type: Object as PropType<{ [key: string]: string }>,
      required: true,
    },
  },
  setup(props) {
    const visibleCount = ref(5);
    const incrementCount = 2;

    const visibleItems = computed(() =>
      props.items.slice(0, visibleCount.value)
    );

    const filteredItem = (item) => {
      const filtered = {};
      for (const key in item) {
        if (props.displayLabels[key]) {
          filtered[props.displayLabels[key]] = item[key];
        }
      }
      return filtered;
    };

    const loadMore = () => {
      visibleCount.value += incrementCount;
    };

    return {
      visibleItems,
      filteredItem,
      loadMore,
    };
  },
});
</script>

import { useState, useCallback } from 'react';

export function useToggleSet(initialValues?: string[] | Set<string>) {
  const [set, setSet] = useState<Set<string>>(() => new Set(initialValues));

  const toggle = useCallback((value: string) => {
    setSet(prev => {
      const next = new Set(prev);
      if (next.has(value)) {
        next.delete(value);
      } else {
        next.add(value);
      }
      return next;
    });
  }, []);

  const has = useCallback((value: string) => {
    return set.has(value);
  }, [set]);

  return [set, toggle, has, setSet] as const;
}

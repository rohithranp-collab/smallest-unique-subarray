# 3934. Smallest Unique Subarray

- **Problem:** [3934. Smallest Unique Subarray](https://leetcode.com/problems/smallest-unique-subarray/description/?envType=daily-question&envId=2026-11-25)
- **Difficulty:** Hard
- **Topics:** Array, Hash Table, Binary Search, Rolling Hash

---

## Problem Summary

Given an integer array `nums`, find the **minimum length** of a contiguous subarray that is **not identical** (same length and same elements in corresponding positions) to any other subarray in `nums`.

### Examples

| Input (`nums`) | Output | Explanation |
| :--- | :--- | :--- |
| `[3, 3, 3]` | `3` | Length 1 and length 2 subarrays repeat; `[3, 3, 3]` appears once. |
| `[2, 1, 2, 3, 3]` | `1` | `[1]` appears only once. |
| `[1, 1, 2, 2, 1]` | `2` | Length 2 subarrays such as `[1, 1]`, `[1, 2]`, `[2, 2]`, and `[2, 1]` each appear once. |

---

## Approach

1. **Binary Search on Subarray Length:**
   If a unique subarray of length `L` exists, any longer subarray containing it is also unique. Feasibility is monotonic (`False` → `True`) as length increases, so we binary search `L` over `[1, len(nums)]`.

2. **Sliding Window + Rolling Hash:**
   For a fixed window length `mid`, compute polynomial rolling hashes across all subarrays of length `mid` in $O(n)$ time and count hash occurrences in a dictionary (`freq`). If any hash has frequency `1`, a unique subarray of length `mid` exists.

---

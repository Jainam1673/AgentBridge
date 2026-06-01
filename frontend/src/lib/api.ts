"use client";

import { useQuery } from "@tanstack/react-query";
import axios from "axios";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8080";

export const usePlatformSummary = () => {
  return useQuery({
    queryKey: ["platform-summary"],
    queryFn: async () => {
      const { data } = await axios.get(`${API_BASE}/analytics/summary`);
      return data;
    },
  });
};

export const useTenantsReadiness = () => {
  return useQuery({
    queryKey: ["tenants-readiness"],
    queryFn: async () => {
      const { data } = await axios.get(`${API_BASE}/analytics/tenants/readiness`);
      return data;
    },
  });
};

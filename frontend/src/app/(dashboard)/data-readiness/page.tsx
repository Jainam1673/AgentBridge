import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { Badge } from "@/components/ui/badge";
import { AlertCircle, CheckCircle2, Info } from "lucide-react";

"use client";

import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { Badge } from "@/components/ui/badge";
import { AlertCircle, CheckCircle2, Info } from "lucide-react";
import { useTenantsReadiness } from "@/lib/api";
import { Skeleton } from "@/components/ui/skeleton";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";

export default function DataReadinessPage() {
  const { data: tenants, isLoading } = useTenantsReadiness();

  const recommendations = [
    { type: "Critical", text: "Populate missing 'Owner' and 'ProjectID' metadata for 1,240 documents in Google Drive." },
    { type: "Medium", text: "Map GitHub issue labels to Jira priority levels for consistent cross-system reporting." },
    { type: "Low", text: "Enable incremental sync for the PostgreSQL 'archive' schema." },
  ];

  if (isLoading) {
    return <div className="p-8"><Skeleton className="h-64 w-full" /></div>;
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold">AI Readiness Assessment</h1>
        <p className="text-muted-foreground">Identifying and resolving data blockers for enterprise-grade AI deployment.</p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Tenant Readiness Scores</CardTitle>
          <CardDescription>Live assessment of tenant data ecosystems</CardDescription>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Tenant</TableHead>
                <TableHead>AI Readiness Score</TableHead>
                <TableHead>Freshness</TableHead>
                <TableHead>Completeness</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {tenants?.map((tenant: any) => (
                <TableRow key={tenant.name}>
                  <TableCell className="font-medium">{tenant.name}</TableCell>
                  <TableCell>
                    <div className="flex items-center gap-2">
                      <Progress value={tenant.score} className="h-2 w-24" />
                      <span>{tenant.score}%</span>
                    </div>
                  </TableCell>
                  <TableCell>{tenant.freshness}</TableCell>
                  <TableCell>{tenant.completeness}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
...

      <div className="grid gap-6 md:grid-cols-3">
        <Card className="md:col-span-2">
          <CardHeader>
            <CardTitle>Actionable Recommendations</CardTitle>
            <CardDescription>Strategic steps to improve your AI Readiness Score</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            {recommendations.map((rec, idx) => (
              <div key={idx} className="flex gap-4 p-4 border rounded-lg bg-muted/30">
                <Badge variant={rec.type === "Critical" ? "destructive" : "secondary"} className="h-fit">
                  {rec.type}
                </Badge>
                <p className="text-sm font-medium">{rec.text}</p>
              </div>
            ))}
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>System Health</CardTitle>
            <CardDescription>Connective tissue status</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="flex items-center justify-between text-sm">
              <span className="flex items-center gap-2"><Info className="h-4 w-4" /> Latency (P95)</span>
              <span className="font-mono">1.2s</span>
            </div>
            <div className="flex items-center justify-between text-sm">
              <span className="flex items-center gap-2"><Info className="h-4 w-4" /> Error Rate</span>
              <span className="font-mono text-green-500">0.02%</span>
            </div>
            <div className="flex items-center justify-between text-sm">
              <span className="flex items-center gap-2"><Info className="h-4 w-4" /> Cost/Session</span>
              <span className="font-mono">$0.04</span>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

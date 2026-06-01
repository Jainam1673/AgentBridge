import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { Badge } from "@/components/ui/badge";
import { AlertCircle, CheckCircle2, Info } from "lucide-react";

export default function DataReadinessPage() {
  const readinessMetrics = [
    { label: "Data Freshness", score: 92, status: "Healthy", description: "All sources synced within the last 24h" },
    { label: "Schema Integrity", score: 85, status: "Warning", description: "3 tables missing primary key definitions" },
    { label: "Metadata Completeness", score: 64, status: "Critical", description: "High volume of documents missing 'Owner' tag" },
    { label: "Redundancy Rate", score: 98, status: "Healthy", description: "Less than 1% duplicate records detected" },
  ];

  const recommendations = [
    { type: "Critical", text: "Populate missing 'Owner' and 'ProjectID' metadata for 1,240 documents in Google Drive." },
    { type: "Medium", text: "Map GitHub issue labels to Jira priority levels for consistent cross-system reporting." },
    { type: "Low", text: "Enable incremental sync for the PostgreSQL 'archive' schema." },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold">AI Readiness Assessment</h1>
        <p className="text-muted-foreground">Identifying and resolving data blockers for enterprise-grade AI deployment.</p>
      </div>

      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
        {readinessMetrics.map((m) => (
          <Card key={m.label}>
            <CardHeader className="pb-2">
              <CardDescription className="flex items-center justify-between">
                {m.label}
                {m.status === "Healthy" ? <CheckCircle2 className="h-4 w-4 text-green-500" /> : <AlertCircle className="h-4 w-4 text-amber-500" />}
              </CardDescription>
              <CardTitle className="text-2xl">{m.score}%</CardTitle>
            </CardHeader>
            <CardContent>
              <Progress value={m.score} className="h-2 mb-2" />
              <p className="text-xs text-muted-foreground">{m.description}</p>
            </CardContent>
          </Card>
        ))}
      </div>

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

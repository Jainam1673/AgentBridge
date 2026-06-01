import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";

export default function DataReadinessPage() {
  const tenants = [
    { name: 'Acme Manufacturing', score: 82, freshness: '92%', completeness: '78%' },
    { name: 'Globex Finance', score: 91, freshness: '98%', completeness: '89%' },
    { name: 'HealthCorp', score: 65, freshness: '72%', completeness: '61%' },
  ];

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Data Readiness Assessment</h1>
      
      <Card>
        <CardHeader>
          <CardTitle>Tenant Readiness Scores</CardTitle>
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
              {tenants.map((tenant) => (
                <TableRow key={tenant.name}>
                  <TableCell className="font-medium">{tenant.name}</TableCell>
                  <TableCell>{tenant.score}%</TableCell>
                  <TableCell>{tenant.freshness}</TableCell>
                  <TableCell>{tenant.completeness}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}

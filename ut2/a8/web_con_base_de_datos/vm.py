from mysql import DB


class VirtualMachine:

    def __init__(self, id):
        self.db = DB("abraham", "79072387cC$", "db_web")
        sql = f"select * from vmachine where id={id}"
        run = self.db.query(sql)
        self.id = run[0]["id"]
        self.name = run[0]["name"]
        self.ram = run[0]["ram"]
        self.cpu = run[0]["cpu"]
        self.hdd = run[0]["hdd"]
        self.os = run[0]["os"]
        self.status = 0
        # self.proc = list()

    def stop(self):
        sql = "update vmachine set status=0 where id=1"
        self.db.run(sql)
        sql = "delete from process where id=1"
        self.db.run(sql)
        self.status = 0
        # self.proc = list()

    def start(self):
        sql = "update vmachine set status=1 where id=1"
        self.db.run(sql)
        self.status = 1

    def suspend(self):
        sql = "update vmachine set status=2 where id=1"
        self.db.run(sql)
        self.status = 2

    def reboot(self):
        self.stop()
        self.start()

    def get_process(self):
        sql = f"select * from process where vmachine_id={self.id}"
        return self.db.query(sql)

    def run(self, pid, ram, cpu, hdd):
        sql = f"insert into process (pid, ram, cpu, hdd, vmachine_id) values ({pid}, {ram}, {cpu}, {hdd}, 1)"
        self.db.run(sql)
        # self.proc.append(
        #    {
        #        "pid": pid,
        #        "ram": ram,
        #        "cpu": cpu,
        #        "hdd": hdd
        #   }
        # )

    def ram_usage(self):
        ram = 0
        for p in self.get_process():
            ram += p["ram"]
        return ram * 100 / self.ram

    def cpu_usage(self):
        cpu = 0
        for p in self.get_process():
            cpu += p["cpu"]
        return cpu * 100 / self.cpu

    def hdd_usage(self):
        hdd = 0
        for p in self.get_process():
            hdd += p["hdd"]
        return hdd * 100 / self.hdd

    def get_status(self):
        if self.status == 0:
            return "Stopped"
        elif self.status == 1:
            return "Running"
        elif self.status == 2:
            return "Suspended"

    def __str__(self):
        return """
{} <{}> [{}]
{:.2f}% RAM used | {:.2f}% CPU used | {:.2f}% HDD used
        """.format(
            self.os,
            self.name,
            self.get_status(),
            self.ram_usage(),
            self.cpu_usage(),
            self.hdd_usage()
        )

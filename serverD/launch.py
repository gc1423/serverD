import click
from serverD.core import serverDcore


server = serverDcore()


@click.group()
def launch_entry():
    pass


@launch_entry.command()
@click.argument("server_name")
def login(server_name):
    server.login(server_name)


@launch_entry.command()
@click.argument("server_name")
@click.argument("local_path")
@click.argument("server_path")
def put(server_name, local_path, server_path):
    server.put(server_name, local_path, server_path)


@launch_entry.command()
@click.argument("server_name")
@click.argument("server_path")
@click.argument("local_path")
def get(server_name, server_path, local_path):
    server.get(server_name, server_path, local_path)


@launch_entry.command()
@click.argument("server_name")
@click.argument("host")
@click.argument("port")
@click.argument("user")
@click.option("--passwd", default=None)
@click.option("--pem", default=None)
def add(server_name, host, port, user, passwd, pem):
    if not passwd and not pem:
        print("passwd or pem, one at least")
        return
    result = server.addServer(server_name, host, port, user, passwd=passwd, pem_path=pem)
    if result:
        print(f"server {server_name} add succeed")


@launch_entry.command()
@click.argument("server_name")
def delete(server_name):
    server.deleteServer(server_name)
    print(f"{server_name} deleted")


# TODO 完善管理界面
# @launch_entry.command()
# @click.pass_context
# def manage(ctx, server_name, server_path, local_path):
#     log_level = "DEBUG" if ctx.obj['DEBUG'] else "INFO"
#     server.get(server_name, server_path, local_path)

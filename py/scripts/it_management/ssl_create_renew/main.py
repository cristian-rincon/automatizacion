import os
import typer

app = typer.Typer()


class CommandsHandler():
    stop_nginx = "sudo /opt/bitnami/ctlscript.sh stop nginx"
    start_nginx = "sudo /opt/bitnami/ctlscript.sh start nginx"
    start_create = 'sudo /opt/bitnami/letsencrypt/lego --tls --email="soporte@grupodot.com"'
    letsencrypt_create = '--path="/opt/bitnami/letsencrypt" run'
    letsencrypt_renew = '--path="/opt/bitnami/letsencrypt" renew --days 90'


domains = [
    "gitlab.grupodot.com",
    "data.gitlab.grupodot.com",
    "retail.gitlab.grupodot.com",
    "health.gitlab.grupodot.com",
    "telcos.gitlab.grupodot.com",
    "oil-gas.gitlab.grupodot.com",
    "registry.gitlab.grupodot.com",
    "insurers.gitlab.grupodot.com",
    "projects.gitlab.grupodot.com",
    "data-team.gitlab.grupodot.com",
    "real-estate.gitlab.grupodot.com",
    "internal-projects.gitlab.grupodot.com",
]

domains_to_create = [f'--domains="{domain}"' for domain in domains]

@app.command()
def server(option: str = typer.Option(..., help="Commands for gitlab nginx administration")):
    if option == "start":
        typer.echo("Starting nginx")
        os.system(CommandsHandler.start_nginx)
    elif option == "stop":
        typer.echo("Shuting down nginx")
        os.system(CommandsHandler.stop_nginx)
    else:
        typer.Abort()


@app.command()
def ssl_certificate(option: str = typer.Argument(..., help="Commands for ssl certificates administration")):
    if option == "create":
        create_certs = f'{CommandsHandler.start_create} {"".join(domains_to_create)} {CommandsHandler.letsencrypt_create}'
        server("stop")
        typer.secho("Creating certificates:", fg=typer.colors.GREEN)
        os.system(create_certs)
        server("start")
    elif option == "renew":
        renew_certs = f'{CommandsHandler.start_create} {"".join(domains_to_create)} {CommandsHandler.letsencrypt_renew}'
        server("stop")
        typer.secho("Renewing certificates:", fg=typer.colors.GREEN)
        os.system(renew_certs)
        server("start")
    else:
        typer.Abort()


@app.command()
def gitlab(option: str = typer.Argument("status", help="Commands for gitlab instance administration")):
    if option == "update":
        typer.secho("Updating system:", fg=typer.colors.GREEN)
        os.system('sudo apt update')
        typer.secho("Updating Gitlab:", fg=typer.colors.GREEN)
        os.system('sudo apt install gitlab-ee')
    elif option == "status":
        os.system('sudo gitlab-ctl status')
    elif option == "restart":
        os.system('sudo gitlab-ctl restart')
    elif option == "reconfigure":
        os.system('sudo gitlab-ctl reconfigure')
    elif option == "config":
        os.system('sudo nano /etc/gitlab/gitlab.rb')
    else:
        typer.Abort()


if __name__ == "__main__":
    app()

document.getElementById("formCredito").addEventListener("submit", async function (e) {
    e.preventDefault(); // Evita recargar la página

    const form = e.target;

    const data = {
        cliente: form.cliente.value,
        monto: parseFloat(form.monto.value),
        tasa_interes: parseFloat(form.tasa_interes.value),
        plazo: parseInt(form.plazo.value),
        fecha_otorgamiento: form.fecha_otorgamiento.value
    };

    try {
        const res = await fetch("/creditos", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        if (res.ok) {
            alert("Crédito registrado correctamente");
            location.reload(); // Refresca la tabla
        } else {
            const error = await res.json();
            alert("Error: " + error.error);
        }
    } catch (err) {
        alert("Error de conexión: " + err);
    }
});

async function eliminarCredito(id) {
    const confirmar = confirm(`¿Estás seguro de eliminar el crédito con ID ${id}?`);

    if (!confirmar) return;

    try {
        const res = await fetch(`/creditos/${id}`, {
            method: "DELETE"
        });

        if (res.ok) {
            alert("Crédito eliminado correctamente");
            location.reload();
        } else {
            const error = await res.json();
            alert("Error al eliminar: " + error.error);
        }
    } catch (err) {
        alert("Error de conexión: " + err.message);
    }
}

function editarCredito(id) {
    // Buscar los valores desde la fila
    const fila = document.querySelector(`button[onclick="editarCredito(${id})"]`).closest("tr");
    const celdas = fila.querySelectorAll("td");

    const formEditar = document.getElementById("formEditar");
    formEditar.id.value = id;
    formEditar.cliente.value = celdas[1].textContent;
    formEditar.monto.value = celdas[2].textContent;
    formEditar.tasa_interes.value = celdas[3].textContent;
    formEditar.plazo.value = celdas[4].textContent;
    formEditar.fecha_otorgamiento.value = celdas[5].textContent;

    document.getElementById("editarContainer").style.display = "block";
    window.scrollTo({ top: formEditar.offsetTop, behavior: 'smooth' });
}

document.getElementById("formEditar").addEventListener("submit", async function (e) {
    e.preventDefault();

    const form = e.target;
    const id = form.id.value;

    const data = {
        cliente: form.cliente.value,
        monto: parseFloat(form.monto.value),
        tasa_interes: parseFloat(form.tasa_interes.value),
        plazo: parseInt(form.plazo.value),
        fecha_otorgamiento: form.fecha_otorgamiento.value
    };

    try {
        const res = await fetch(`/creditos/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        if (res.ok) {
            alert("Crédito actualizado correctamente");
            location.reload();
        } else {
            const error = await res.json();
            alert("Error: " + error.error);
        }
    } catch (err) {
        alert("Error de conexión: " + err.message);
    }
});

function cancelarEdicion() {
    document.getElementById("editarContainer").style.display = "none";
}



<script lang="ts">
	let fileInput: HTMLInputElement;
	let error = '';
	let file: File;
	let fileName = '';
	let isDragging = false;

	const handleOnDragOver = (e) => {
		event.preventDefault();
		// console.log(e);
        isDragging=true
	};

    const handleOnDragLeave = (e) => {
		event.preventDefault();
        isDragging=false
    }

    const handleDragDrop = (e: DragEvent & { currentTarget: EventTarget & HTMLButtonElement }) => {
		event.preventDefault();
        isDragging=false
        console.log(e.dataTransfer.files[0]);
        const file = e.dataTransfer.files[0] as File;

        handleFiles(file)


    }


	const handleFileInput = (event: Event & { currentTarget: EventTarget & HTMLInputElement }) => {
		const file = event?.target?.files?.[0];
		handleFiles(file);
	};

	const handleFiles = async(newFile: File) => {
		error = '';

		if (!newFile.name.endsWith('.mp4')) {
			error = 'صيغة الملف غير مدعومة';
			return;
		}
		file = newFile;
		fileName = newFile.name;

        if(!file){
            error = "لايوجد ملف"
            return
        }

        const formData = new FormData();
        formData.append("file",file)

        try{

            const response = await fetch("URL",{
                method:"POST",
                body:formData
            });

            if(response.ok){
                console.log("تم الرقع بنجاح");
                //handle response here: show transcript, summary, 
            } 
            
        }catch(e){
            error = "حصل خطأ أثناء الرقع";
            throw new Error(`Failed to upload: ${error}`);
        }



	}
</script>

<header>
	<nav class="primary-nav">
		<div class="flex-10">
			<img src="images/logo.png" alt="" />
			<p>جوهر</p>
		</div>
	</nav>
</header>
<main class="wrapper">
	<div class="bg-secondary">
		<div class="upload-section">
			<div class="drag-and-drop flex-10" on:dragover={handleOnDragOver} on:drop={handleDragDrop} on:dragleave={handleOnDragLeave}>
				<img src="images/meet.png" alt="" />
				<p>يمكنك سحب مقطع الإجتماع إلى هنا.</p>
				<input
					type="file"
					accept=".mp4"
					class="hidden"
					bind:this={fileInput}
					on:change={handleFileInput}
				/>
			</div>
            <p style="color:red;">
                {error}
                
            </p>

			<p>أو</p>
			<button type="button" on:click={()=>fileInput.click()}>تصفح الملفات</button>
		</div>
	</div>
</main>

<style>
	img {
		max-inline-size: 100%;
		display: block;
		margin: 10px;
	}

	p {
		color: var(--secondary);
		font-size: 1.5rem;
		font-weight: bold;
	}

	.primary-nav {
		background-color: var(--bg-secondary);
		padding-inline: 60px;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.primary-nav p {
		color: var(--primary);
		font-weight: bold;
		font-size: 1.75rem;
	}

	.flex-10 {
		display: flex;
		gap: 10px;
		justify-content: center;
	}

	.wrapper {
		max-inline-size: 1000px;
		margin-inline: auto;
	}

	.bg-secondary {
		background-color: var(--bg-secondary);
		border-radius: 25px;
		padding: 20px;
		margin-inline: 20px;
		margin-block: 100px;
	}

	.upload-section {
		background-color: #1e1e1e;
		border-radius: 25px;
		padding: 20px;
		margin: 20px;
		text-align: center;
	}

	.drag-and-drop {
		border: solid var(--primary);
		border-radius: 25px;
		padding: 50px;
		margin: 20px;
	}

	.drag-and-drop p {
		color: #757575;
		font-size: 1.5rem;
		font-weight: bold;
	}

	button {
		color: #757575;
		font-size: 1.5rem;
		font-weight: bold;
		background-color: var(--bg-secondary);
		border: solid 2px var(--primary);
		border-radius: 25px;
		padding: 20px;
        cursor:pointer;
        transition:0.5s;

	}
	
	button:hover {
    background-color: var(--primary);
}

	.hidden {
		visibility: hidden;
	}
</style>

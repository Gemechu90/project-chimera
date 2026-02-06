from skills.content_generator.skill import generate_content

def test_generate():
    out = generate_content("AI")
    assert "text" in out

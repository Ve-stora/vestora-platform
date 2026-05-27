from fastapi import APIRouter

router = APIRouter()

@router.get("/modules")
def get_education_modules():
    """Get list of educational modules"""
    return {
        "modules": [
            {
                "id": 1,
                "title": "Getting Started with Investing",
                "description": "Learn the basics of investing in Uganda's capital markets",
                "lessons": 5
            },
            {
                "id": 2,
                "title": "Understanding Stocks",
                "description": "Deep dive into stock fundamentals and trading",
                "lessons": 6
            },
            {
                "id": 3,
                "title": "Portfolio Management",
                "description": "How to build and manage a diversified portfolio",
                "lessons": 4
            }
        ]
    }

@router.get("/modules/{module_id}")
def get_module(module_id: int):
    """Get specific educational module"""
    return {
        "id": module_id,
        "title": "Module Title",
        "lessons": [
            {"id": 1, "title": "Lesson 1", "content": "..."}
        ]
    }
# Day 04 – Evaluating Expressions and Operator Precedence in Python

## 1. What Is an Expression?

An expression is a combination of constants, variables, and operators that evaluates to a value.

A value or a standalone variable is also considered an expression, whereas a standalone operator is not an expression.

### Components of an Expression

- **Operands:** Values or variables on which an operator performs an operation.
- **Operators:** Symbols that perform specific operations on operands.
- **Expression result:** The value obtained after evaluating an expression.

## 2. Evaluating Expressions

Evaluating an expression means determining its final value by performing the required operations in the correct order.

When an expression contains multiple operators, Python follows operator precedence rules to decide which operation must be performed first.

The evaluation process involves identifying the operators, applying precedence rules, performing the operations in the appropriate order, and obtaining the final result.

## 3. What Is Operator Precedence?

Operator precedence refers to the priority or hierarchy of operators in an expression.

When an expression contains more than one operator, the operator with higher precedence is evaluated before an operator with lower precedence.

Operator precedence determines the order of evaluation and helps Python calculate expressions correctly.

## 4. Precedence of Arithmetic Operators

The following table shows the precedence of the arithmetic operators covered in this lesson, from highest to lowest.

| Priority | Operator | Operation |
|---|---|---|
| 1 | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `*` | Multiplication |
| 3 | `/` | Division |
| 3 | `//` | Floor division |
| 3 | `%` | Modulus |
| 4 | `+` | Addition |
| 4 | `-` | Subtraction |

### Explanation of Precedence

**Parentheses `()`**

Expressions inside parentheses are evaluated first. Parentheses can change the normal order of evaluation.

**Exponentiation `**`**

Exponentiation calculates a number raised to a power. It has higher precedence than multiplication, division, floor division, modulus, addition and subtraction.

**Multiplication, Division, Floor Division and Modulus**

These operators have equal precedence. When they appear together, Python generally evaluates them from left to right.

- `*` performs multiplication.
- `/` performs division and returns a floating-point result.
- `//` performs floor division.
- `%` returns the remainder after division.

**Addition and Subtraction**

Addition and subtraction have equal precedence and lower precedence than multiplication, division, floor division and modulus. When they appear together, Python generally evaluates them from left to right.

## 5. Role of Parentheses in Expressions

Parentheses are used to override the normal precedence of operators.

The expression inside parentheses is evaluated first, even if its operators would normally have lower precedence than operators outside the parentheses.

Parentheses make expressions easier to understand and help specify the intended order of operations.

## 6. Associativity of Operators

Associativity determines the direction in which operators of equal precedence are evaluated.

### Left-to-Right Associativity

Most arithmetic operators with equal precedence are evaluated from left to right.

This applies to multiplication, division, floor division, modulus, addition and subtraction when they occur at the same precedence level.

### Right-to-Left Associativity

Exponentiation (`**`) is evaluated from right to left.

This means that when multiple exponentiation operators occur in one expression, the operation on the right is evaluated first.

## 7. Important Rules for Evaluating Expressions

Follow these rules when evaluating an expression:

1. Evaluate expressions inside parentheses first.
2. Evaluate exponentiation according to its precedence and right-to-left associativity.
3. Evaluate multiplication, division, floor division and modulus before addition and subtraction.
4. For operators of equal precedence, follow their associativity.
5. Continue evaluating until the final value is obtained.

## 8. Common Mistakes to Avoid

- Performing addition before multiplication when no parentheses require it.
- Ignoring parentheses while evaluating an expression.
- Confusing division (`/`) with floor division (`//`).
- Assuming exponentiation is evaluated from left to right.
- Assuming all operators have equal precedence.
- Forgetting that operators of equal precedence are generally evaluated according to their associativity.

## 9. Quick Revision

- An expression is a combination of values, variables and operators that evaluates to a value.
- Operator precedence determines which operation is performed first.
- Parentheses can override the normal order of evaluation.
- Exponentiation has higher precedence than multiplication and division.
- Multiplication, division, floor division and modulus share the same precedence.
- Addition and subtraction share the same precedence.
- Most arithmetic operators of equal precedence are evaluated from left to right.
- Exponentiation is evaluated from right to left.

---
